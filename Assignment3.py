{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question1\n",
    "lst=[]\n",
    "elements=int(input(\"Enter the no.of.elements\"))\n",
    "for i in range(elements):\n",
    "    n=int(input(\"Enter the numbers:\"))\n",
    "    lst.append(n)\n",
    "    print(\"new list is:\",lst)\n",
    "temp=len(lst)\n",
    "print(len(lst))\n",
    "lst.sort()\n",
    "\n",
    "print(\"Largest Number in the list\",lst[temp-1])\n",
    "print(\"Second largest Number in the list \",lst[temp-2])\n",
    "\n",
    "lst[0],lst[-1] = lst[-1], lst[0]\n",
    "print(\"After swapping, the list is:\",lst[0],lst[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question2\n",
    "lst1 = [2, 8, 5, 0]\n",
    "lst2 = [6, 3, 1, 3]\n",
    "result=lst1+lst2\n",
    "print(result)\n",
    "result.sort()\n",
    "print(\"After Sorting the list is :\",result)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question3\n",
    "L1 = {1, 2, 2, 5}\n",
    "L2 = {2, 5, 7, 9}\n",
    "\n",
    "print(L1.intersection(L2))\n",
    "print(L1.union(L2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question4\n",
    "l=[]\n",
    "elem=int(input(\"Enter the no.of.elements\"))\n",
    "for i in range(elem):\n",
    "    n=int(input(\"Enter the numbers:\"))\n",
    "    l.append(n)\n",
    "    print(\"updated list is :\",l)\n",
    "length=len(l)\n",
    "print(len(l))\n",
    "print(\"The 3rd and 6th element\",l[2],l[5])\n",
    "print(\"First 5 elements\",l[:5])\n",
    "print(\"From 7 elements\",l[7:8])\n",
    "l[0]='x'\n",
    "l[1]='y'\n",
    "print(\"After Changing first and second elements \",l[0],l[1])\n",
    "print(\"The no.of elements in the list is \",len(l))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question5\n",
    "n=int(input(\"Enter the number of elements to be in the list:\"))\n",
    "b=[]\n",
    "for i in range(0,n):\n",
    "    a=int(input(\"Element: \"))\n",
    "    b.append(a)\n",
    "c=[]\n",
    "d=[]\n",
    "for i in b:\n",
    "    if(i%2==0):\n",
    "        c.append(i)\n",
    "    else:\n",
    "        d.append(i)\n",
    "c.sort()\n",
    "d.sort()\n",
    "count1=0\n",
    "count2=0\n",
    "for k in c:\n",
    "    count1=count1+1\n",
    "for j in d:\n",
    "    count2=count2+1\n",
    "print(\"Largest even number:\",c[count1-1])\n",
    "print(\"Largest odd number\",d[count2-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question6\n",
    "l=int(input(\"Enter the lower range:\"))\n",
    "u=int(input(\"Enter the upper range:\"))\n",
    "a=[(x,x**2) for x in range(l,u+1)]\n",
    "a.sort()\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question7\n",
    "import random\n",
    "l=[]\n",
    "n=int(input(\"Enter number of elements\"))\n",
    "for j in range(n):\n",
    "    l.append(random.randint(1,20))\n",
    "print('Randomised list is: ',l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question8\n",
    "import math\n",
    "print(\"Enter the coefficients of the polynomial\")\n",
    "lst=[]\n",
    "for i in range(0,3):\n",
    "    n=int(input(\"Enter the coefficient:\"))\n",
    "    lst.append(n)\n",
    "x=int(input(\"Enter the value of x:\"))\n",
    "sum=0\n",
    "j=2\n",
    "for i in range(0,2):\n",
    "    while(j>0): \n",
    "        sum=sum+(lst[i]*math.pow(x,j))\n",
    "        break\n",
    "    j=j-1\n",
    "sum=sum+lst[2]\n",
    "print(\"The value of the polynomial is:\",sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question9\n",
    "l=int(input(\"Enter lower range: \"))\n",
    "u=int(input(\"Enter upper range: \"))\n",
    "a=[]\n",
    "a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question10\n",
    "a=[]\n",
    "num= int(input(\"Enter the number of elements in list:\"))\n",
    "for x in range(0,num):\n",
    "    element=int(input(\"Enter element\" + str(x+1) + \":\"))\n",
    "    a.append(element)\n",
    "b=[sum(a[0:x+1]) for x in range(0,len(a))]\n",
    "print(\"The original list is: \",a)\n",
    "print(\"The new list is: \",b)\n"
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
