input_file = r"source_words\S-YA.txt"
output_file = "S-YAnew.txt"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        clean_line = line.strip()
        if clean_line:             
            f_out.write(clean_line + "\n")
