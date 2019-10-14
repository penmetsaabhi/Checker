import calendar
import math
import click
import os
import subprocess
def check_two_files(name1,name2):
    fd1=open(name1)
    fd2=open(name2)
    out=open("result.txt","w")
    lines1=fd1.readlines()
    lines2=fd2.readlines()
    output=""
    if(len(lines1) != len(lines2)):
        output += "linesMisMatch\n"

    for i in range(min(len(lines1),len(lines2))):
        if(lines1[i] == lines2[i]):
            continue
        else:
            output += lines1[i][0:len(lines1[i])-1] + " ------- " + lines2[i][0:len(lines2[i])-1] + "\n"
    if(output==""):
        output ="Both are same"
    else:
        output = "Outputs are Not equal \n" + output
    out.write(output)
    fd1.close()
    fd2.close()
    out.close()

def main():
    fd = open("input.txt")
    data1 , write1 = os.pipe()
    data2 ,write2 =os.pipe()
    input_data= " "
    for line in fd.readlines():
        input_data = input_data + line
    input_data = str.encode(input_data)
    os.write(write1,input_data )
    os.write(write2,input_data)
    os.close(write1)
    os.close(write2)
    subprocess.check_output("g++ Program1.cpp -o object1;./object1 > output1.txt", stdin=data1, shell=True)
    subprocess.check_output("g++ Program2.cpp -o object2;./object2 > output2.txt", stdin=data2, shell=True)
    check_two_files("output1.txt","output2.txt")
    fd.close()
if __name__ == '__main__':
    main()