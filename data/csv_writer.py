import csv

with open('employee_file.csv', 'w') as employee_file:
  fieldnames = ['firstname', 'lastname', 'pay']
  fieldnames = ['firstname', 'lastname', 'pay']
  writer = csv.DictWriter(employee_file, fieldnames)

  writer.writeheader()
  writer.writerow({'firstname': 'John', 'lastname': 'Doe', 'pay': 50000})
  writer.writerow({'firstname': 'Albert', 'lastname': 'Heijn', 'pay': 56000})
  writer.writerow({'firstname': 'Khadija', 'lastname': 'Lee', 'pay': 64000})
  writer.writerow({'firstname': 'Diane', 'lastname': 'Anderson', 'pay': 64500})
  writer.writerow({'firstname': 'Richtje', 'lastname': 'van de Peppel', 'pay': 68000})
  writer.writerow({'firstname': 'Felicienne', 'lastname': 'Desnoyer', 'pay': 74000})
  writer.writerow({'firstname': 'Claire', 'lastname': 'Duperré', 'pay': 67000})
  writer.writerow({'firstname': 'Chinwendu', 'lastname': 'Chiabuotu', 'pay': 69000})
  writer.writerow({'firstname': 'Ezinma', 'lastname': 'Obi', 'pay': 79000})
  writer.writerow({'firstname': 'Cino', 'lastname': 'Cino', 'pay': 65000})
  writer.writerow({'firstname': 'Abdul-Fattah', 'lastname': 'Wahab', 'pay': 76000})
  writer.writerow({'firstname': 'Nadir', 'lastname': 'William', 'pay': 64000})
  writer.writerow({'firstname': 'Novalie', 'lastname': 'Eriksson', 'pay': 74000})
  writer.writerow({'firstname': 'Makoto', 'lastname': 'Taihei', 'pay': 84000})
  writer.writerow({'firstname': 'Bogumiła', 'lastname': 'Bogumiła', 'pay': 66000})
  writer.writerow({'firstname': 'Isabela', 'lastname': 'Fernandes', 'pay': 65900})
  writer.writerow({'firstname': 'Anna', 'lastname': 'Schmitz', 'pay': 77800})
  writer.writerow({'firstname': 'Nadine', 'lastname': 'Krause', 'pay': 79000})
  writer.writerow({'firstname': 'Nkemakonam', 'lastname': 'Alabi', 'pay': 75000})
  writer.writerow({'firstname': 'Yusuf', 'lastname': 'Ibrahim', 'pay': 66000})
  writer.writerow({'firstname': 'Christine', 'lastname': 'Björk', 'pay': 69000})