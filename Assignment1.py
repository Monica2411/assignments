{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the first no.4\n",
      "Enter the second no.5\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "#sum of two numbers\n",
    "n1=int(input(\"Enter the first no.\"))\n",
    "n2=int(input(\"Enter the second no.\"))\n",
    "n3=n1+n2\n",
    "print(n3)"
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
      "Enter a number5\n",
      "Prime number\n"
     ]
    }
   ],
   "source": [
    "#Prime no.or not\n",
    "num=int(input(\"Enter a number\"))\n",
    "i=2\n",
    "flag=0\n",
    "while i<num:\n",
    "    if(num%i==0):\n",
    "        flag=1\n",
    "        break\n",
    "    i = i + 1\n",
    "if(flag==0):    \n",
    "    print(\"Prime number\")\n",
    "else:\n",
    "    print(\"Not a Prime number\")"
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
      "Enter the height5\n",
      "Enter the base6\n",
      "Area of the triangle is 5.500000\n"
     ]
    }
   ],
   "source": [
    "#Area of a triangle\n",
    "h=float(input(\"Enter the height\"))\n",
    "b=float(input(\"Enter the base\"))\n",
    "Area=(h+b)/2\n",
    "print(\"Area of the triangle is %f\"%Area)"
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
      "After swaping a = 2 and b = 1\n"
     ]
    }
   ],
   "source": [
    "#swap two numbers\n",
    "a=1\n",
    "b=2\n",
    "a, b = b, a\n",
    "print(\"After swaping a = %d and b = %d\" %(a, b))\n"
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
      "The solutons are (-6+0.07493486755176124j) and (-6-0.07493486755176124j)\n"
     ]
    }
   ],
   "source": [
    "#Quadratic equation solution\n",
    "import cmath\n",
    "a=4\n",
    "b=6\n",
    "c=8\n",
    "d=(b*b)-(4*a*c)\n",
    "s1=(-b+cmath.sqrt(d)/(4*a*c))\n",
    "s2=(-b-cmath.sqrt(d)/(4*a*c))\n",
    "print('The solutons are {0} and {1}'.format(s1,s2))"
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
      "Enter the year7\n",
      "The year is not a leap year 7\n"
     ]
    }
   ],
   "source": [
    "#Leap Year\n",
    "year=int(input(\"Enter the year\"))\n",
    "if (year % 4) == 0:\n",
    "    if (year % 100) == 0:\n",
    "        if (year % 400) == 0:\n",
    "            print(\"The year is a leap year %d\" %year)\n",
    "        else:\n",
    "            print(\"The year is not a leap year %d\" %year)\n",
    "    else:\n",
    "        print(\"The year is a leap year %d\" %year)\n",
    "else:\n",
    "    print(\"The year is not a leap year %d\" %year)\n",
    "                    "
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
      "Input a number: -4\n",
      "It is a negative number\n"
     ]
    }
   ],
   "source": [
    "#Postive,Negative or Zero\n",
    "num = int(input(\"Input a number: \"))\n",
    "if num > 0:\n",
    "    print(\"It is positive number\")\n",
    "elif num == 0:\n",
    "    print(\"It is Zero\")\n",
    "else:\n",
    "    print(\"It is a negative number\")\n",
    "   "
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
      "Enter a number: 50\n",
      "The sum of first n natural numbers is 1275\n"
     ]
    }
   ],
   "source": [
    "#sum of first n natural nos.\n",
    "n=int(input(\"Enter a number: \"))\n",
    "sum = 0\n",
    "while(n > 0):\n",
    "    sum=sum+n\n",
    "    n=n-1\n",
    "print(\"The sum of first n natural numbers is\",sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number5\n",
      "Odd number\n"
     ]
    }
   ],
   "source": [
    "#Odd or even\n",
    "n=int(input(\"Enter the number\"))\n",
    "m=n%2\n",
    "if m>0:\n",
    "    print(\"Odd number\")\n",
    "else:\n",
    "    print(\"Even number\")"
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
      "Enter the number5\n",
      "120\n"
     ]
    }
   ],
   "source": [
    "#factorial\n",
    "n=int(input(\"Enter the number\"))\n",
    "def fact(n):\n",
    "    if n==1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n*fact(n-1)\n",
    "\n",
    "print(fact(n))\n"
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
      "Enter the number4\n",
      "Enter the no of multiples you want10\n",
      "4 x 1 = 4\n",
      "4 x 2 = 8\n",
      "4 x 3 = 12\n",
      "4 x 4 = 16\n",
      "4 x 5 = 20\n",
      "4 x 6 = 24\n",
      "4 x 7 = 28\n",
      "4 x 8 = 32\n",
      "4 x 9 = 36\n",
      "4 x 10 = 40\n"
     ]
    }
   ],
   "source": [
    "#Multiplication Table\n",
    "n=int(input(\"Enter the number\"))\n",
    "m=int(input(\"Enter the no of multiples you want\"))\n",
    "\n",
    "for i in range(1,m+1):\n",
    "    print(n,'x',i,'=',n*i)"
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
      "Select operation.\n",
      "1.Add\n",
      "2.Subtract\n",
      "3.Multiply\n",
      "4.Divide\n",
      "Enter choice(1/2/3/4):1\n",
      "Enter first number: 2\n",
      "Enter second number: 3\n",
      "2 + 3 = 5\n"
     ]
    }
   ],
   "source": [
    "#Calculator\n",
    "def add(x, y):\n",
    "    return x + y\n",
    "\n",
    "def subtract(x, y):\n",
    "    return x - y\n",
    "\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "\n",
    "def divide(x, y):\n",
    "    return x / y\n",
    "\n",
    "print(\"Select operation.\")\n",
    "print(\"1.Add\")\n",
    "print(\"2.Subtract\")\n",
    "print(\"3.Multiply\")\n",
    "print(\"4.Divide\")\n",
    "\n",
    "choice = input(\"Enter choice(1/2/3/4):\")\n",
    "\n",
    "n1 = int(input(\"Enter first number: \"))\n",
    "n2 = int(input(\"Enter second number: \"))\n",
    "\n",
    "if choice == '1':\n",
    "    print(n1,\"+\",n2,\"=\", add(n1,n2))\n",
    "\n",
    "elif choice == '2':\n",
    "    print(n1,\"-\",n2,\"=\", subtract(n1,n2))\n",
    "\n",
    "elif choice == '3':\n",
    "    print(n1,\"*\",n2,\"=\", multiply(n1,n2))\n",
    "\n",
    "elif choice == '4':\n",
    "    print(n1,\"/\",n2,\"=\", divide(n1,n2))\n",
    "else:\n",
    "    print(\"Invalid input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of series5\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter the number of series\"))\n",
    "\n",
    "number1=0\n",
    "number2=1\n",
    "i=0\n",
    "print(number1)\n",
    "print(number2)\n",
    "while(i<num-2):\n",
    "    n=number1+number2\n",
    "    print(n)\n",
    "    number1=number2\n",
    "    number2=n\n",
    "    i=i+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the integer4\n",
      "Enter the integer5\n",
      "Enter the integer6\n",
      "6 is the maximum \n",
      "4 is the minimum \n"
     ]
    }
   ],
   "source": [
    "number1 =  int(input(\"Enter the integer\"))\n",
    "number2 =  int(input(\"Enter the integer\"))\n",
    "number3 =  int(input(\"Enter the integer\"))\n",
    "\n",
    "if((number1>=number2) and (number1>=number3)):\n",
    "    print(\"%d is the maximum \" % number1)\n",
    "elif((number2>=number1) and (number2>=number3)):\n",
    "    print(\"%d is the maximum \" % number2)\n",
    "elif((number3>=number1) and (number3>=number2)):\n",
    "    print(\"%d is the maximum \" % number3)\n",
    "\n",
    "if((number1<=number2) and (number1<=number3)):\n",
    "    print(\"%d is the minimum \" % number1)\n",
    "elif((number2<=number1) and (number2<=number3)):\n",
    "    print(\"%d is the minimum \" % number2)\n",
    "elif((number3<=number1) and (number3<=number2)):\n",
    "    print(\"%d is the minimum \" % number3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Enter the km 746\n",
      "convertion into miles :  463.542766\n"
     ]
    }
   ],
   "source": [
    "k = float(input(\" Enter the km \"))\n",
    "\n",
    "m =  k * 0.621371\n",
    "\n",
    "print(\"convertion into miles :  %f\"  %m )"
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
      " please enter the celsius temperature 65\n",
      "the farenheit convertion :  149.000000\n"
     ]
    }
   ],
   "source": [
    "celsius = float(input(\" please enter the celsius temperature \"))\n",
    "\n",
    "faren =  celsius * 1.8 +32\n",
    "\n",
    "print(\"the farenheit convertion :  %f\" %faren )"
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
      "enter the number6\n",
      "0b110 in binary.\n",
      "0o6 in octal.\n",
      "0x6 in hexadecimal.\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"enter the number\"))\n",
    "\n",
    "print(bin(n),\"in binary.\")\n",
    "print(oct(n),\"in octal.\")\n",
    "print(hex(n),\"in hexadecimal.\")"
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
