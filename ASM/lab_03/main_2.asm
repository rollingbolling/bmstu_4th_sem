PUBLIC output_X
EXTRN X: byte

;res segment 
DSEG2 SEGMENT PARA public 'DATA'
    SYMB db byte 
DSEG2 ENDS

;code segment
CSEG SEGMENT PARA PUBLIC 'CODE'
    assume CS:CSEG, ES:DSEG2
output_X proc near
    ;DATASEG
    MOV AX, DSEG2
    MOV es, AX

    ;trans to lower reg
    MOV AL, X
    add al, 20h     ;уменьшение на 20 в hex (по ascii)
    mov symb, al
    
    ;output
    MOV DL, 10      ;перевод на след строку
    int 21H
    MOV AH, 2       ;указываем адресс функции вывода символа
    mov dl, symb    ;указываем адресс результата перевода
    int 21H
    
    ret
output_X endp
CSEG ENDS
END
