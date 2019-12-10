# Average 3

def student_avr(score_1, score_2, score_3, score_4):
	'''Calculates a student's average score'''
	# Calculate the average with weights 2, 3, 4 e 1 respectively
	weights = 2 + 3 + 4 + 1
	avr_score = ((score_1 * 2) + (score_2 * 3) + (score_3 * 4) + score_4) / weights
	return avr_score

def second_call(avr_score, score_5):
	'''Calculates average score with the second call test'''
	new_score = (avr_score + score_5) / 2
	return new_score

scores = input().split()
score_1 = float(scores[0])
score_2 = float(scores[1])
score_3 = float(scores[2])
score_4 = float(scores[3])
avr_score = student_avr(score_1, score_2, score_3, score_4)
print('Media: {:.1f}'.format(avr_score))

if avr_score >= 7.0:
	message = 'Aluno aprovado.'
elif avr_score < 5.0:
	message = 'Aluno reprovado.'
elif avr_score >= 5.0 and avr_score <= 6.9:
	message = 'Aluno em exame.'
print(message)

if message == 'Aluno em exame.':
	score_5 = float(input())
	new_score = second_call(avr_score, score_5)
	print('Nota do exame: {:.1f}'.format(score_5))
	if new_score >= 5.0:
		message = 'Aluno aprovado.'
	elif new_score < 5.0:
		message = 'Aluno reprovado.'
	print(message)
	print('Media final: {:.1f}'.format(new_score))
