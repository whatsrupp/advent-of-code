class PassportBatchChecker:

    current_validity_matrix = None
    current_line = None

    def __init__(self, batch_file="input.txt"):
        self.batch_file = batch_file

    def check_batch(self):
        batch_file = open(self.batch_file, 'r')
        lines = batch_file.readlines()

        blank_validity_matrix = {
          "byr": False,
          "iyr": False,
          "eyr": False,
          "hgt": False,
          "hcl": False,
          "ecl": False,
          "pid": False
          # "cid": False
        }

        validity_matrix = blank_validity_matrix.copy()
        valid_passport_count = 0

        for line in lines:
          line = line.replace("\n", "")

          if not line:
            print(validity_matrix)
            is_valid = True
            for value in validity_matrix.values():
               if value == False:
                 is_valid = False 
                 break
            
            if is_valid:
              valid_passport_count += 1

            validity_matrix = blank_validity_matrix.copy()
            continue

          fields = line.split(" ")
          for field in fields:
            attribute = field[0:3]
            validity_matrix[attribute] = True
        
        return valid_passport_count




passport_batch_checker = PassportBatchChecker()
print(passport_batch_checker.check_batch())
