
import click
VOWELS = "aeiou"

def to_piglatin(eng):
		if eng[0] in vowels:
			return eng + "way"
		else if not eng[1] in vowels:
			return eng[1:] + eng[0] + "ay"
		else:
			return eng[2:] + eng[0:2] +"ay"
