import os

script_dir = os.path.dirname(os.path.abspath(__file__))
vault_name = os.path.basename(script_dir)
vault_path = os.path.join(script_dir, vault_name + ".obsidian")


if not os.path.exists(vault_path):
    os.makedirs(vault_path)
    print(f"Created directory: {vault_path}")

directories_to_scan = [
    os.path.join(script_dir, d) for d in os.listdir(script_dir)
    if os.path.isdir(os.path.join(script_dir, d)) and not d.startswith(".")
]

pdf_files = []
for directory in directories_to_scan:
    if os.path.exists(directory):
        pdf_files.extend([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".pdf")])

for pdf_path in pdf_files:
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    parent_directory = os.path.basename(os.path.dirname(pdf_path))

    note_path = os.path.join(vault_path, f"{pdf_name}.md")

    if os.path.exists(note_path):
        print(f"Note already exists, skipping: {note_path}")
        continue

    note_content = f"Link to the PDF: [{pdf_name}](file:///{os.path.abspath(pdf_path)})\n\n"
    note_content += "## Notes\n\n"

    note_content += f'\n## Tags\n\n#{parent_directory.replace(" ", "_").lower()}'

    with open(note_path, "w") as note_file:
        note_file.write(note_content)

    print(f"Created note: {note_path}")
