.686
.MODEL FLAT, C
.STACK

.CODE

myStrcpy proc
	mov esi, ecx; ecx=src
	mov edi, edx; edx=dst
	mov ecx, eax; eax=len

	cmp edi, esi
	je exit

not_equal: ;строки не перекрываются
	cmp edi, esi
	jl copy

	mov eax, edi
	sub eax, esi

	cmp eax, ecx
	jge copy

comp_copy: ;строки перекрываются
		add edi, ecx; перемещение в конец строки
		add esi, ecx
		sub esi, 1
		sub edi, 1
		std; df = 1 уменьшение инд регистров

		copy:
	rep movsb; из esi в edi пока df==0 длина==ecx
	cld; df = 0 увеличение инд регистров (сброс флага)

exit:
	ret
myStrcpy endp

end