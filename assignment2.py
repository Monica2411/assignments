{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 1 is an armstrong Number \n",
      " 153 is an armstrong Number \n",
      " 370 is an armstrong Number \n",
      " 371 is an armstrong Number \n",
      " 407 is an armstrong Number \n"
     ]
    }
   ],
   "source": [
    "#Question1\n",
    "def Armstri(n):\n",
    "    temp = n\n",
    "   \n",
    "    d=0\n",
    "    num=0\n",
    "    while (temp!=0):\n",
    "        d=temp%10\n",
    "        num+=(d**3)\n",
    "        temp=temp//10\n",
    "    if(num==n):\n",
    "        print(\" %d is an armstrong Number \" %n)\n",
    "        \n",
    "for i in range(1,500):\n",
    "    Armstri(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Question2\n",
    "n= int(input(\"Enter the number\"))\n",
    "\n",
    "def fact(n):\n",
    "    if(n==1):\n",
    "        return 1\n",
    "    else:\n",
    "        return n * fact(n-1)\n",
    "    \n",
    "fact(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "  if n == 1 or n == 2:\n",
    "    return 1\n",
    "  else:\n",
    "    return (fibonacci(n - 1) + (fibonacci(n - 2)))\n",
    "\n",
    "print(fibonacci(5))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the stringDHue65\n",
      "The number of digits characters is:\n",
      "2\n",
      "The number of uppercase characters is:\n",
      "2\n",
      "The number of uppercase characters is:\n",
      "2\n",
      "The length of the String is:  7\n",
      "DHue65ing\n"
     ]
    }
   ],
   "source": [
    "#Question3\n",
    "str=input(\"Enter the string\")\n",
    "count1=0\n",
    "count2=0\n",
    "count3=0\n",
    "for i in str:\n",
    "        if(i.isdigit()):\n",
    "            count1=count1+1\n",
    "        elif(i.islower()):\n",
    "            count2=count2+1\n",
    "        elif(i.isupper()):\n",
    "            count3=count3+1\n",
    "print(\"The number of digits characters is:\")\n",
    "print(count1)\n",
    "print(\"The number of uppercase characters is:\")\n",
    "print(count2)\n",
    "print(\"The number of uppercase characters is:\")\n",
    "print(count3)\n",
    "k=len(str)+1\n",
    "print(\"The length of the String is: \",k)\n",
    "str = str + 'ing'\n",
    "print(str)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter string:thydufh\n",
      "Modified string:\n",
      "hhyduft\n"
     ]
    }
   ],
   "source": [
    "#Question4\n",
    "def change(string):\n",
    "      return string[-1:] + string[1:-1] + string[:1]\n",
    "string = input(\"Enter string:\")\n",
    "print(\"Modified string:\")\n",
    "print(change(string))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Modified string is:\n",
      "Teqikbonfxjmsoe h aydg\n",
      "{'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1}\n"
     ]
    }
   ],
   "source": [
    "#Question5\n",
    "def modify(string):  \n",
    "      final = \"\"   \n",
    "      for i in range(len(string)):  \n",
    "            if i % 2 == 0:  \n",
    "                  final = final + string[i]  \n",
    "      return final\n",
    "string=\"The quick brown fox jumps over the lazy dog\"\n",
    "print(\"Modified string is:\")\n",
    "print(modify(string))\n",
    "def word_count(str):\n",
    "    counts = dict()\n",
    "    words = str.split()\n",
    "\n",
    "    for word in words:\n",
    "        if word in counts:\n",
    "            counts[word] += 1\n",
    "        else:\n",
    "            counts[word] = 1\n",
    "\n",
    "    return counts\n",
    "\n",
    "print( word_count(string))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tahw\n",
      "atadesabmapS\n"
     ]
    }
   ],
   "source": [
    "#Question6\n",
    "def reverse_string(str1):\n",
    "    if len(str1) % 4 == 0:\n",
    "       return ''.join(reversed(str1))\n",
    "    return str1\n",
    "\n",
    "print(reverse_string('what'))\n",
    "print(reverse_string('Spambasedata'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hey\n",
      "I\n",
      "am\n",
      "are\n",
      "fine\n",
      "how\n",
      "you\n"
     ]
    }
   ],
   "source": [
    "#Question7\n",
    "def sortLexo(my_string):\n",
    "\n",
    "    words = my_string.split()\n",
    "    words.sort()\n",
    "    for i in words:\n",
    "        print( i ) \n",
    " \n",
    "my_string = \"Hey how are you \" \\\n",
    "              \"I am fine\"\n",
    "sortLexo(my_string)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      ">  Gandhi famously led Indians in challenging the\n",
      "> British-imposed salt tax with the 400 km (250 mi)\n",
      "> Dandi Salt March in 1930, and later in calling for\n",
      "> the British to Quit India in 1942. He was\n",
      "> imprisoned for many years, upon many occasions, in\n",
      "> both South Africa and India. He lived modestly in\n",
      "> a self-sufficient residential community and wore\n",
      "> the traditional Indian dhoti and shawl, woven with\n",
      "> yarn hand-spun on a charkha\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Question8\n",
    "import textwrap\n",
    "sample_text ='''\n",
    "    Gandhi famously led Indians in challenging the British-imposed salt tax with the 400 km (250 mi) Dandi Salt March in 1930, and later in calling for the British to Quit India in 1942. He was imprisoned for many years, upon many occasions, in both South Africa and India. He lived modestly in a self-sufficient residential community and wore the traditional Indian dhoti and shawl, woven with yarn hand-spun on a charkha\n",
    "    '''\n",
    "text_without_Indentation = textwrap.dedent(sample_text)\n",
    "wrapped = textwrap.fill(text_without_Indentation, width=50)\n",
    "final_result = textwrap.indent(wrapped, '> ')\n",
    "print()\n",
    "print(final_result)\n",
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current character P position at 0\n",
      "Current character o position at 1\n",
      "Current character s position at 2\n",
      "Current character t position at 3\n",
      "Current character e position at 4\n",
      "Current character r position at 5\n",
      "Current character i position at 6\n",
      "Current character o position at 7\n",
      "Current character r position at 8\n",
      "4\n",
      "['o', 'e', 'i', 'o']\n"
     ]
    }
   ],
   "source": [
    "#Question9\n",
    "str1 = \"Posterior\"\n",
    "for index, char in enumerate(str1):\n",
    "    print(\"Current character\", char, \"position at\", index )\n",
    "    \n",
    "def vowel(text):\n",
    "    vowels = \"aeiuoAEIOU\"\n",
    "    print(len([letter for letter in text if letter in vowels]))\n",
    "    print([letter for letter in text if letter in vowels])\n",
    "vowel(str1);\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter comma separated inputgreat,jam,bat\n",
      "bat,great,jam\n"
     ]
    }
   ],
   "source": [
    "#Question10\n",
    "string = input(\"Enter comma separated input\")\n",
    "words = [word for word in string.split(\",\")]\n",
    "print(\",\".join(sorted(list(set(words)))))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
