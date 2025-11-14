import os
import shutil
import time

def list_files(path):
    print(f"\n📁 Listing files in: {path}\n")
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print(f"[DIR]  {item}")
        else:
            print(f"      {item}")
    print("\n")

def create_folder(path, folder_name):
    new_path = os.path.join(path, folder_name)
    try:
        os.mkdir(new_path)
        print(f"✅ Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print("⚠️ Folder already exists.")
    except Exception as e:
        print("❌ Error:", e)

def delete_item(path, name):
    full_path = os.path.join(path, name)
    if os.path.isdir(full_path):
        shutil.rmtree(full_path)
        print(f"🗑️ Folder '{name}' deleted successfully.")
    elif os.path.isfile(full_path):
        os.remove(full_path)
        print(f"🗑️ File '{name}' deleted successfully.")
    else:
        print("❌ Item not found.")

def rename_item(path, old_name, new_name):
    old_path = os.path.join(path, old_name)
    new_path = os.path.join(path, new_name)
    try:
        os.rename(old_path, new_path)
        print(f"✏️ Renamed '{old_name}' → '{new_name}' successfully.")
    except Exception as e:
        print("❌ Error:", e)

def copy_item(path, source, destination):
    source_path = os.path.join(path, source)
    dest_path = os.path.join(path, destination)
    try:
        if os.path.isdir(source_path):
            shutil.copytree(source_path, dest_path)
        else:
            shutil.copy(source_path, dest_path)
        print(f"📄 '{source}' copied to '{destination}'.")
    except Exception as e:
        print("❌ Error:", e)

def main():
    current_path = os.getcwd()

    while True:
        print("\n" + "="*50)
        print("     🗂️  PYTHON FILE MANAGER  🗂️")
        print("="*50)
        print(f"📍 Current Directory: {current_path}")
        print("\n1️⃣  List Files and Folders")
        print("2️⃣  Create Folder")
        print("3️⃣  Delete File/Folder")
        print("4️⃣  Rename File/Folder")
        print("5️⃣  Copy File/Folder")
        print("6️⃣  Change Directory")
        print("7️⃣  Exit")
        print("-"*50)

        choice = input("👉 Enter your choice (1-7): ").strip()

        if choice == '1':
            list_files(current_path)
            input("Press Enter to continue...")

        elif choice == '2':
            folder = input("Enter new folder name: ")
            create_folder(current_path, folder)
            time.sleep(1)

        elif choice == '3':
            name = input("Enter file/folder name to delete: ")
            delete_item(current_path, name)
            time.sleep(1)

        elif choice == '4':
            old = input("Enter current name: ")
            new = input("Enter new name: ")
            rename_item(current_path, old, new)
            time.sleep(1)

        elif choice == '5':
            src = input("Enter file/folder name to copy: ")
            dest = input("Enter new name or destination path: ")
            copy_item(current_path, src, dest)
            time.sleep(1)

        elif choice == '6':
            new_path = input("Enter path to change directory: ")
            if os.path.exists(new_path):
                current_path = new_path
                print("📂 Directory changed successfully.")
            else:
                print("❌ Path not found.")
            time.sleep(1)

        elif choice == '7':
            print("👋 Exiting File Manager... Goodbye!")
            time.sleep(1)
            break

        else:
            print("❗ Invalid choice! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
