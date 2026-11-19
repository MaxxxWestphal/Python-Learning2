# Problem 1



def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        machines: dict mapping machine name -> log file name

    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """

    counts = {}

    with open("info.log", "w") as info_file, \
         open("warning.log", "w") as warning_file, \
         open("error.log", "w") as error_file:

        for machine in sorted(machines):
            counts[machine] = {
                "INFO": 0,
                "WARNING": 0,
                "ERROR": 0
            }
            with open(machines[machine], "r") as log_file:
                for line in log_file:
                    line = line.rstrip("\n")

                    if line.strip() == "":
                        continue

                    output_line = f"{machine} | {line}\n"

                    if "[INFO]" in line:
                        info_file.write(output_line)
                        counts[machine]["INFO"] += 1

                    elif "[WARNING]" in line:
                        warning_file.write(output_line)
                        counts[machine]["WARNING"] += 1

                    elif "[ERROR]" in line:
                        error_file.write(output_line)
                        counts[machine]["ERROR"] += 1
    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""

    print("SECURITY LOG REPORT")
    print("=" * 40)

    total_info = 0
    total_warning = 0
    total_error = 0
    total_entries = 0
    for machine in counts:
        info = counts[machine]["INFO"]
        warning = counts[machine]["WARNING"]
        error = counts[machine]["ERROR"]
        entries = info + warning + error
        total_info += info
        total_warning += warning
        total_error += error
        total_entries += entries

        if error >= 2:
            status = "CRITICAL"
        elif error >= 1 or warning >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"

        print(
            f"{machine}: {entries} entries | INFO {info} | "
            f"WARNING {warning} | ERROR {error} | Status: {status}"
        )

    print("-" * 40)
    print(
        f"Total: {total_entries} entries | INFO {total_info} | "
        f"WARNING {total_warning} | ERROR {total_error}"
    )

    print("Errors (see error.log):")

    with open(error_file, "r") as f:
        for line in f:
            print("  " + line.rstrip())
#Test code


with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

counts = split_logs({
    "server_a": "server_a.log",
    "server_b": "server_b.log"
})

print(counts)

with open("warning.log", "r") as f:
    print(f.read())

print_report(counts)
            
# Problem 2


import json
import pickle
import os


def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""

    incidents = []

    with open(csv_file, "r") as f:
        lines = f.readlines()

    for line in lines[1:]:  # skip header
        line = line.strip()

        if not line:
            continue

        incident_id, machine, severity, description = line.split(",")

        incidents.append({
            "id": int(incident_id),
            "machine": machine,
            "severity": severity,
            "description": description
        })

    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""

    summary = {
        "total": len(incidents),
        "by_machine": {},
        "by_severity": {},
        "high_ids": []
    }

    for incident in incidents:
        machine = incident["machine"]
        severity = incident["severity"]
        summary["by_machine"][machine] = (
            summary["by_machine"].get(machine, 0) + 1
        )

        summary["by_severity"][severity] = (
            summary["by_severity"].get(severity, 0) + 1
        )

        if severity == "high":
            summary["high_ids"].append(incident["id"])

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)
    return summary


def archive(incidents, folder):
    """
    Pickle all incidents and write one JSON file per machine
    into folder.
    """

    os.makedirs(folder, exist_ok=True)
    pickle_path = os.path.join(folder, "incidents.pkl")

    with open(pickle_path, "wb") as f:
        pickle.dump(incidents, f)

    machines = {}
    for incident in incidents:
        machine = incident["machine"]

        if machine not in machines:
            machines[machine] = []
        machines[machine].append(incident)

    for machine in machines:
        file_path = os.path.join(folder, f"{machine}.json")

        with open(file_path, "w") as f:
            json.dump(machines[machine], f, indent=2)
    return sorted(os.listdir(folder))


def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    pickle_path = os.path.join(folder, "incidents.pkl")
    with open(pickle_path, "rb") as f:
        incidents = pickle.load(f)

    return incidents

#Test code
with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")

incidents = load_incidents("incidents.csv")

print(len(incidents))
print(incidents[0])

summary = save_summary(incidents, "summary.json")

print(summary)

with open("summary.json", "r") as f:
    print(json.load(f) == summary)

print(archive(incidents, "archive"))

with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])

restored = load_archive("archive")

print(restored == incidents)

# Problem 3

import os
import shutil


def organize(folder):
    """Move files into logs/, data/, pickles/, other/ by extension."""

    result = {
        "logs": [],
        "data": [],
        "pickles": [],
        "other": []
    }

    for subfolder in result:
        os.makedirs(os.path.join(folder, subfolder), exist_ok=True)

    for name in os.listdir(folder):
        path = os.path.join(folder, name)

        if not os.path.isfile(path):
            continue

        ext = os.path.splitext(name)[1].lower()

        if ext == ".log":
            target = "logs"
        elif ext in [".csv", ".json"]:
            target = "data"
        elif ext == ".pkl":
            target = "pickles"
        else:
            target = "other"

        shutil.move(
            path,
            os.path.join(folder, target, name)
        )

        result[target].append(name)

    for key in result:
        result[key].sort()

    return result


def create_backup(source_dir, backup_root, label):
    """
    Copy source_dir to backup_root/backup_<label>;
    return the new path.
    """

    os.makedirs(backup_root, exist_ok=True)

    backup_dir = os.path.join(
        backup_root,
        f"backup_{label}"
    )

    shutil.copytree(source_dir, backup_dir)

    return backup_dir


def verify_backup(source_dir, backup_dir):
    """
    Return True if every file under source_dir
    is in backup_dir with the same size.
    """

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)

            rel_path = os.path.relpath(
                source_file,
                source_dir
            )

            backup_file = os.path.join(
                backup_dir,
                rel_path
            )

            if not os.path.exists(backup_file):
                return False
            if os.path.getsize(source_file) != os.path.getsize(backup_file):
                return False
    return True


def cleanup_old_backups(backup_root, keep):
    """
    Delete all but the newest keep backups;
    return sorted names deleted.
    """

    backups = []

    for name in os.listdir(backup_root):
        path = os.path.join(backup_root, name)

        if os.path.isdir(path):
            backups.append(name)

    backups.sort()
    to_delete = backups[:-keep]

    for folder in to_delete:
        shutil.rmtree(
            os.path.join(backup_root, folder)
        )

    return sorted(to_delete)



#Test code

for old in ["workspace", "backups"]:
    if os.path.exists(old):
        shutil.rmtree(old)

os.mkdir("workspace")

for name in [
    "a.log",
    "b.log",
    "incidents.csv",
    "summary.json",
    "incidents.pkl",
    "notes.txt"
]:
    with open(os.path.join("workspace", name), "w") as f:
        f.write(f"Test file: {name}\n")

print(organize("workspace"))

print(sorted(os.listdir("workspace")))

for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:
    path = create_backup("workspace", "backups", label)
    print(os.path.basename(path), verify_backup("workspace", path))

os.remove(
    os.path.join(
        "backups",
        "backup_2026-10-03",
        "logs",
        "a.log"
    )
)

print(
    verify_backup(
        "workspace",
        os.path.join(
            "backups",
            "backup_2026-10-03"
        )
    )
)

print(cleanup_old_backups("backups", 2))

print(sorted(os.listdir("backups")))
