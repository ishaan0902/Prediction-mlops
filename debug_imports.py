# debug_current_state.py - Show exactly what's in your project
import os
import sys

def debug_project_structure():
    print("🔍 DEBUGGING PROJECT STRUCTURE - NO BULLSHIT")
    print("=" * 60)
    
    # Current working directory
    cwd = os.getcwd()
    print(f"📁 Current working directory: {cwd}")
    
    # List root directory contents
    print(f"\n📂 Root directory contents:")
    try:
        root_files = os.listdir('.')
        for item in sorted(root_files):
            if os.path.isdir(item):
                print(f"   📁 {item}/")
            else:
                print(f"   📄 {item}")
    except Exception as e:
        print(f"   ❌ Error reading root: {e}")
    
    # Check for Data directory (with capital D)
    print(f"\n🔍 Checking for Data directory:")
    data_dirs_to_check = ['Data', 'data', 'DATA']
    
    for data_dir in data_dirs_to_check:
        if os.path.exists(data_dir):
            print(f"   ✅ Found: {data_dir}/")
            try:
                files = os.listdir(data_dir)
                print(f"      Contents: {files}")
                
                # Check specifically for CSV files
                csv_files = [f for f in files if f.endswith('.csv')]
                if csv_files:
                    print(f"      📊 CSV files: {csv_files}")
                    
                    # Show details of each CSV
                    for csv_file in csv_files:
                        csv_path = os.path.join(data_dir, csv_file)
                        size = os.path.getsize(csv_path)
                        print(f"         📄 {csv_file}: {size:,} bytes")
                else:
                    print(f"      ⚠️  No CSV files found")
            except Exception as e:
                print(f"      ❌ Error reading {data_dir}: {e}")
        else:
            print(f"   ❌ Not found: {data_dir}/")
    
    # Check the exact path from your original code
    original_path = r'Data\predictive_maintenance.csv'
    print(f"\n🎯 Checking your original path: {original_path}")
    if os.path.exists(original_path):
        size = os.path.getsize(original_path)
        print(f"   ✅ File exists! Size: {size:,} bytes")
        
        # Try to read first few lines
        try:
            import pandas as pd
            df = pd.read_csv(original_path, nrows=5)
            print(f"   📊 Columns: {list(df.columns)}")
            print(f"   📊 Shape (first 5 rows): {df.shape}")
            print(f"   📊 Sample data:")
            print(df.head())
        except Exception as e:
            print(f"   ❌ Error reading CSV: {e}")
    else:
        print(f"   ❌ File does NOT exist at this path!")
    
    # Check artifacts directory
    print(f"\n📂 Checking artifacts directory:")
    if os.path.exists('artifacts'):
        files = os.listdir('artifacts')
        print(f"   ✅ Exists, contents: {files}")
        
        for file in files:
            if file.endswith('.csv') or file.endswith('.pkl'):
                size = os.path.getsize(os.path.join('artifacts', file))
                print(f"      📄 {file}: {size:,} bytes")
    else:
        print(f"   ❌ artifacts/ directory does not exist")
    
    # Check if there are any CSV files anywhere
    print(f"\n🔍 Searching for ALL CSV files in project:")
    csv_files_found = []
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and common build directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
        
        for file in files:
            if file.endswith('.csv'):
                full_path = os.path.join(root, file)
                size = os.path.getsize(full_path)
                csv_files_found.append((full_path, size))
    
    if csv_files_found:
        print(f"   📊 Found {len(csv_files_found)} CSV files:")
        for path, size in csv_files_found:
            print(f"      📄 {path}: {size:,} bytes")
    else:
        print(f"   ❌ NO CSV files found anywhere in the project!")
    
    print("=" * 60)
    print("🎯 CONCLUSION:")
    
    if os.path.exists(original_path):
        print(f"✅ Your dataset exists at the expected location")
        print(f"✅ The training should work with real data")
    else:
        print(f"❌ Your dataset is MISSING from the expected location")
        print(f"❌ You need to place 'predictive_maintenance.csv' in the 'Data' directory")
        if csv_files_found:
            print(f"💡 But I found other CSV files - maybe one of these is your dataset?")
        else:
            print(f"💡 No CSV files found anywhere - you need to add your dataset")

if __name__ == "__main__":
    debug_project_structure()