from subprocess import check_output


t = check_output(['ls', '-l']).decode('utf-8')
print(t)