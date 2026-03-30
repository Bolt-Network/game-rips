import os

def split_file(filename, chunk_size_mb=15):
    if not os.path.exists(filename):
        print(f"File {filename} not found!")
        return 0
    
    # Get the directory of the input file
    target_dir = os.path.dirname(filename)
    
    chunk_size = chunk_size_mb * 1024 * 1024
    file_prefix = "wasm.part." if ".wasm" in filename else "data.part."
    
    parts_count = 0
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            # Create the output name relative to the target directory
            output_name = os.path.join(target_dir, f"{file_prefix}{parts_count:02d}")
            with open(output_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            
            print(f"Created: {output_name}")
            parts_count += 1
    
    if parts_count > 0:
        os.remove(filename)
        print(f"Deleted original file: {filename}")
    return parts_count

# Your specific filenames
base_dir = "99-nights/Build/"
wasm_file = os.path.join(base_dir, "287e54c54d31f22e0512fb5822936c51.wasm.br")
data_file = os.path.join(base_dir, "da4ce0d553e82f86fba06d5fd7e11abd.data.br")

print("Starting split...")
wasm_parts = split_file(wasm_file)
data_parts = split_file(data_file)
print(f"\nDone! WASM parts: {wasm_parts}, DATA parts: {data_parts}")