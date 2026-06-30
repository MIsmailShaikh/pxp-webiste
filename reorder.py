import os

file_path = "workforce-os.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

markers = [
    "<!-- INTELLIGENT HRM PIPELINE SECTION -->",
    "<!-- Core Features Section (Attendance Hub) -->",
    "<!-- Role-Based Dashboards Section -->",
    "<!-- Deep-Dive Modules (Bento Grid) -->",
    "<!-- Complete Ecosystem Directory -->",
    "<!-- Intelligent Automation Workflows Section -->",
    "<!-- Enterprise Security & Privacy Section -->",
    "<!-- Biometric Hardware Compatibility Marquee -->",
    "<!-- The White-Label Advantage Section -->",
    "<!-- Integration Ecosystem Section -->",
    "<!-- Footer -->"
]

# Find indices of all markers
indices = {}
for m in markers:
    idx = content.find(m)
    if idx == -1:
        print(f"Error: Could not find marker {m}")
        exit(1)
    indices[m] = idx

# Determine the sections by sorting the markers by index
sorted_markers = sorted(indices.keys(), key=lambda k: indices[k])

# Extract the sections
sections = {}
for i in range(len(sorted_markers)):
    start_idx = indices[sorted_markers[i]]
    if i < len(sorted_markers) - 1:
        end_idx = indices[sorted_markers[i+1]]
    else:
        end_idx = len(content) # footer goes to end
    sections[sorted_markers[i]] = content[start_idx:end_idx]

# Extract the header (everything before the first marker)
header = content[:indices[sorted_markers[0]]]

# Reconstruct in the new order
new_order = [
    "<!-- INTELLIGENT HRM PIPELINE SECTION -->",
    "<!-- Core Features Section (Attendance Hub) -->",
    "<!-- Role-Based Dashboards Section -->",
    "<!-- Deep-Dive Modules (Bento Grid) -->",
    "<!-- Intelligent Automation Workflows Section -->",
    "<!-- The White-Label Advantage Section -->",
    "<!-- Integration Ecosystem Section -->",
    "<!-- Complete Ecosystem Directory -->",
    "<!-- Biometric Hardware Compatibility Marquee -->",
    "<!-- Enterprise Security & Privacy Section -->",
    "<!-- Footer -->"
]

new_content = header
for m in new_order:
    new_content += sections[m]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Reordering complete.")
