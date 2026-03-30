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
base_dir = "fishit/https_\_\pub-2d868f15a1824cc8a2ec51069ed41c6f.r2.dev"
wasm_file = os.path.join(base_dir, "fish_it_44cc2589b32d6efc0a45a3b388d705ba.wasm.br")


print("Starting split...")
wasm_parts = split_file(wasm_file)
print(f"\nDone! WASM parts: {wasm_parts}")