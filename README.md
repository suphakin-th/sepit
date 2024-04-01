# SEPIT
### This is programimg for seperate Q&A string in txt file, on local directory and export to Excel file.

### Example: data in txt file
```text
Q: การใช้งานห้องติวเตอร์มีข้อจำกัดในเรื่องของการนำเข้าอาหารหรือเครื่องดื่มหรือไม่?
A: บางสถานที่อาจมีข้อจำกัดในการนำเข้าอาหารหรือเครื่องดื่มในห้องติวเตอร์ โปรดปฏิบัติตามกฎระเบียบของแต่ละสถานที่

Q: การจองห้องติวเตอร์สามารถทำได้หลายช่วงเวลาในวันเดียวกันหรือไม่?
A: สามารถทำการจองห้องติวเตอร์ได้หลายช่วงเวลาในวันเดียวกัน โดยใช้ช่วงเวลาที่ว่างอยู่

Q: การใช้งานห้องติวเตอร์มีข้อจำกัดในเรื่องของการใช้งานโทรศัพท์มือถือหรือไม่?
A: บางสถานที่อาจมีข้อจำกัดในการใช้งานโทรศัพท์มือถือในห้องติวเตอร์ โปรดปฏิบัติตามกฎระเบียบของแต่ละสถานที่

...
```

Or you can look at example in txt file on local
## Requirement for use this code.

```text
et-xmlfile==1.1.0
numpy==1.26.4
openpyxl==3.1.2
pandas==2.2.1
python-dateutil==2.9.0.post0
pytz==2024.1
six==1.16.0
tzdata==2024.1
```

## How to use it
 1. Pull this repo to your folder
 2. run this command
 ```bash
 sudo python3 -m pip insatll -r requirement.txt
 ```
 3. After command install done call function for use it
  ```bash
 python3 sepit.py
 ```


Have a nice day.