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

not_equal:
	cmp edi, esi
	jl copy

	mov eax, edi
	sub eax, esi

	cmp eax, ecx
	jge copy

comp_copy:
		add edi, ecx; ����������� � �����
		add esi, ecx
		sub esi, 1
		sub edi, 1
		std; df = 1

		copy:
	rep movsb
	cld; df = 0

exit:
	ret
myStrcpy endp

end