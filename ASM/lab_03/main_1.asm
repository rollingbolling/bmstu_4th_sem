;из двух модулей, в которых объявить по сегменту кода, которые
;должны объединяться в единый. В первом модуле ввести
;заглавную букву латинского алфавита, в другом - вывод строчного
;варианта той же буквы с новой строки.

EXTRN output_X: near

;stack segment
SSEG SEGMENT PARA STACK 'STACK'
    DB 100 DUP(0)
SSEG ENDS

;data segment
DSEG1 SEGMENT PARA public 'DATA'
    X DB byte dup(0)
DSEG1 ENDS

;main code segment
CSEG SEGMENT PARA public 'CODE'
    ASSUME CS:CSEG, DS:DSEG1, SS:SSEG 
MAIN:
    ;DATASEG
    MOV AX, DSEG1
    MOV DS, AX

    ;echoed input
    mov ah, 01h ;указание номера функции для ввода при помощи прерывания
    mov dx, 0
    int 21h     ;вызов функции
    mov x, al
    
    call output_X

    MOV AH, 4CH
    INT 21H
CSEG ENDS
PUBLIC X
END MAIN
