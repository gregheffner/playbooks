import sys
from collections import defaultdict

import yaml

RESOURCE_FIELDS = {
    "serviceAccountName": "ServiceAccount",
    "namespace": "Namespace",
    "configMap": "ConfigMap",
    "configMapRef": "ConfigMap",
    "secret": "Secret",
    "secretRef": "Secret",
    "persistentVolumeClaim": "PersistentVolumeClaim",
    "claimName": "PersistentVolumeClaim",
    "name": "Service",  # For Service kind only
}


# Helper to recursively search for resource references
def find_references(obj, refs, parent_kind=None):
    if isinstance(obj, dict):
        for k, v in obj.items():
            # Special case: serviceAccountName
            if k == "serviceAccountName" and isinstance(v, str):
                refs["ServiceAccount"].add(v)
            # Special case: namespace
            if k == "namespace" and isinstance(v, str):
                refs["Namespace"].add(v)
            # ConfigMap and Secret references
            if k in ("configMap", "configMapRef", "secret", "secretRef") and isinstance(
                v, dict
            ):
                name = v.get("name")
                if name:
                    refs[RESOURCE_FIELDS[k]].add(name)
            # Volumes
            if k == "volumes" and isinstance(v, list):
                for vol in v:
                    if "configMap" in vol:
                        name = vol["configMap"].get("name")
                        if name:
                            refs["ConfigMap"].add(name)
                    if "secret" in vol:
                        name = vol["secret"].get("secretName")
                        if name:
                            refs["Secret"].add(name)
                    if "persistentVolumeClaim" in vol:
                        name = vol["persistentVolumeClaim"].get("claimName")
                        if name:
                            refs["PersistentVolumeClaim"].add(name)
            # envFrom
            if k == "envFrom" and isinstance(v, list):
                for env in v:
                    if "configMapRef" in env:
                        name = env["configMapRef"].get("name")
                        if name:
                            refs["ConfigMap"].add(name)
                    if "secretRef" in env:
                        name = env["secretRef"].get("name")
                        if name:
                            refs["Secret"].add(name)
            # env
            if k == "env" and isinstance(v, list):
                for env in v:
                    if "valueFrom" in env:
                        value_from = env["valueFrom"]
                        if "configMapKeyRef" in value_from:
                            name = value_from["configMapKeyRef"].get("name")
                            if name:
                                refs["ConfigMap"].add(name)
                        if "secretKeyRef" in value_from:
                            name = value_from["secretKeyRef"].get("name")
                            if name:
                                refs["Secret"].add(name)
            # For Service kind, get service name
            if parent_kind == "Service" and k == "metadata" and isinstance(v, dict):
                name = v.get("name")
                if name:
                    refs["Service"].add(name)
            # Recurse
            find_references(v, refs, parent_kind)
    elif isinstance(obj, list):
        for item in obj:
            find_references(item, refs, parent_kind)


def main():
    if len(sys.argv) != 2:
        print("Usage: python k8s_resource_references.py <deployment.yaml>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, "r") as f:
        docs = list(yaml.safe_load_all(f))

    refs = defaultdict(set)
    for doc in docs:
        kind = doc.get("kind")
        find_references(doc, refs, kind)

    print("\nRequired resources referenced in", filename)
    for resource, names in refs.items():
        if names:
            print(f"- {resource}:")
            for name in sorted(names):
                print(f"    {name}")


if __name__ == "__main__":
    main()
