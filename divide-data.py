def split_file(input_file, lines_per_file):
    # เปิดไฟล์ input.txt เพื่ออ่านข้อมูล
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # คำนวณจำนวนไฟล์ที่จะต้องสร้าง
    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file
    
    # แบ่งข้อมูลและเขียนลงไฟล์ใหม่
    for i in range(num_files):
        start = i * lines_per_file
        end = start + lines_per_file
        part_lines = lines[start:end]
        
        # สร้างชื่อไฟล์ใหม่ เช่น output_1.txt, output_2.txt, ...
        output_file = f'output_{i + 1}.txt'
        
        # เขียนข้อมูลลงไฟล์ใหม่
        with open(output_file, 'w', encoding='utf-8') as output:
            output.writelines(part_lines)
    
    print(f'Successfully split {total_lines} lines into {num_files} files.')

# เรียกใช้ฟังก์ชั่น split_file โดยให้ไฟล์ input.txt และแบ่ง 49 บรรทัดต่อไฟล์ (CF อัพสูงสุดได้ 49)
split_file('input.txt', 49)

# ต้องสร้างไฟล์ input.txt ก่อนใช้งานแล้ววางข้อมูลที่ต้องการจะแบ่งลงไฟล์
