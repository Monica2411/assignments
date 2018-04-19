{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the no of students10\n",
      "Enter the Roll no12\n",
      "Enter the namerose\n",
      "Enter the Roll no34\n",
      "Enter the nametulip\n",
      "Enter the Roll no30\n",
      "Enter the namejasmine\n",
      "Enter the Roll no41\n",
      "Enter the namemonica\n",
      "Enter the Roll no65\n",
      "Enter the namemourya\n",
      "Enter the Roll no78\n",
      "Enter the nameshyamala\n",
      "Enter the Roll no37\n",
      "Enter the namemadhu\n",
      "Enter the Roll no76\n",
      "Enter the namejack\n",
      "Enter the Roll no50\n",
      "Enter the namefer\n",
      "Enter the Roll no29\n",
      "Enter the nameian\n",
      "('12', 'rose')\n",
      "('34', 'tulip')\n",
      "('30', 'jasmine')\n",
      "('41', 'monica')\n",
      "('65', 'mourya')\n",
      "('78', 'shyamala')\n",
      "('37', 'madhu')\n",
      "('76', 'jack')\n",
      "('50', 'fer')\n",
      "('29', 'ian')\n"
     ]
    }
   ],
   "source": [
    "#Question1\n",
    "dict = {}\n",
    "\n",
    "num = int(input(\"Enter the no of students\"))\n",
    "\n",
    "for i in range(0,num):\n",
    "    num1=input(\"Enter the Roll no\")\n",
    "   \n",
    "    \n",
    "    name=input(\"Enter the name\")\n",
    "    dict[num1]=name\n",
    "\n",
    "for j in dict.items():\n",
    "    \n",
    "    print(j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Concatenated dictionary is:\n",
      "{'A': 1, 'B': 2, 'C': 3, 'D': 4}\n"
     ]
    }
   ],
   "source": [
    "#Question2\n",
    "dic1={'A':1,'B':2}\n",
    "dic2={'C':3, 'D' :4}\n",
    "dic1.update(dic2)\n",
    "print(\"Concatenated dictionary is:\")\n",
    "print(dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the key to be searched2\n",
      "2   light\n"
     ]
    }
   ],
   "source": [
    "#Question3\n",
    "my_dict = {1:'thunder', 2:'light'}\n",
    "key=int(input(\"Enter the key to be searched\"))\n",
    "check=0\n",
    "for i in my_dict.keys():\n",
    "    if(key==i):\n",
    "        check=1\n",
    "        print(i , \" \" ,my_dict[i])\n",
    "if(check==0):\n",
    "    print(\"Not found\")"
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
      "Enter a number:3\n",
      "{1: 1, 2: 4, 3: 9}\n"
     ]
    }
   ],
   "source": [
    "#Question4\n",
    "num=int(input(\"Enter a number:\"))\n",
    "dict={x:x*x for x in range(1,num+1)}\n",
    "print(dict)"
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
      "466\n"
     ]
    }
   ],
   "source": [
    "#Question5\n",
    "dict = {'number1':56,'number2':3,'number3':407}\n",
    "print(sum(dict.values()))\n"
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
      "250\n"
     ]
    }
   ],
   "source": [
    "#Question6\n",
    "dict={'A':5,'B':5,'C':10}\n",
    "s=1\n",
    "for i in dict:    \n",
    "    s=s*dict[i]\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Santa', 'cricket')\n",
      "('Candy', 'hockey')\n",
      "('Betty', 'baseball')\n",
      "('Dawn', 'football')\n"
     ]
    }
   ],
   "source": [
    "#Question7\n",
    "names = [\"Santa\", \"Candy\", \"Betty\", \"Dawn\", \"Lopel\"]\n",
    "sport = [\"cricket\", \"hockey\", \"baseball\", \"football\"]\n",
    "names_interest = zip(names,sport)\n",
    "\n",
    "for i in names_interest:\n",
    "    print(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter string:hello hi hey hi bye hello\n",
      "('hello', 2)\n",
      "('hi', 2)\n",
      "('hey', 1)\n",
      "('hi', 2)\n",
      "('bye', 1)\n",
      "('hello', 2)\n"
     ]
    }
   ],
   "source": [
    "#Question8\n",
    "str=input(\"Enter string:\")\n",
    "l=[]\n",
    "l=str.split()\n",
    "total=[l.count(p) for p in l]\n",
    "my_d=zip(l,total)\n",
    "for i in my_d:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the no of entries3\n",
      "Enter the stringhelloworld\n",
      "Enter the stringheydear\n",
      "Enter the stringhow are you\n",
      "('h', 'how are you')\n"
     ]
    }
   ],
   "source": [
    "#Question9\n",
    "dict = {}\n",
    "\n",
    "n = int(input(\"Enter the no of entries\"))\n",
    "\n",
    "for i in range(0,n):\n",
    "    \n",
    "    \n",
    "    name=input(\"Enter the string\")\n",
    "    dict[name[0]]=name\n",
    "\n",
    "for j in dict.items():\n",
    "    \n",
    "    print(j)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the no of students10\n",
      "Enter the namerose\n",
      "Enter the marks10\n",
      "Enter the nametulip\n",
      "Enter the marks20\n",
      "Enter the namejasmine\n",
      "Enter the marks30\n",
      "Enter the namemonica\n",
      "Enter the marks40\n",
      "Enter the namemourya\n",
      "Enter the marks57\n",
      "Enter the nameshyamala\n",
      "Enter the marks39\n",
      "Enter the namemadhu\n",
      "Enter the marks74\n",
      "Enter the namerohan\n",
      "Enter the marks93\n",
      "Enter the namejohn\n",
      "Enter the marks74\n",
      "Enter the nameian\n",
      "Enter the marks100\n",
      "10\n",
      "100\n",
      "20\n",
      "30\n",
      "39\n",
      "40\n",
      "57\n",
      "74\n",
      "74\n",
      "93\n"
     ]
    }
   ],
   "source": [
    "#Question10\n",
    "dict = {}\n",
    "\n",
    "n = int(input(\"Enter the no of students\"))\n",
    "\n",
    "for i in range(0,n):\n",
    "  \n",
    "    \n",
    "    name=input(\"Enter the name\")\n",
    "    \n",
    "    \n",
    "    marks=input(\"Enter the marks\")\n",
    "    dict[name]=marks\n",
    "\n",
    "for j in sorted(dict.values()):\n",
    "    \n",
    "    print(j)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
