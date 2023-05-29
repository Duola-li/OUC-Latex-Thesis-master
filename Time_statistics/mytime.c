#include <stdio.h>

#include <stdlib.h>

#include <windows.h>

int main(int argc, char *argv[])

{
    if(argc == 1)
    {//第一次执行，记录开始
        system("python -c \"print('\\n', '-'*20 ) \" >> log.txt");
        system("echo %date%  %time% >> log.txt");
        system("python -c \"print('~')\" >> log.txt");

    }
    else
    {
        system("echo %date%  %time% >> log.txt");
        Beep(523,500);

        Beep(587,500);

        Beep(659,500);

        Beep(698,500);

        Beep(784,500);

        Beep(880,500);

        Beep(980,500);

        Beep(1060,500);

//        Sleep(500);

//        Beep(523,500);
//
//        Beep(587,500);
//
//        Beep(659,500);

        Beep(698,500);

        Beep(784,500);

    }

    return 0;

}
