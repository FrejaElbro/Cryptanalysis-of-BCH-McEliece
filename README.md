# Cryptanalysis-of-BCH-McEliece
The code used for the article "An Algebraic Attack Against McEliece-like Cryptosystems Based on BCH Codes"

This code can be used to break a McEliece-like cryptosystem, where the Goppa code is replaced by a permuted narrow sense primitive BCH code. 


More specifically, our attack recovers the secret key given the public key outputted by the following key generation function:
Key generation:
 - Input: (p,s,m,r), where s,m,r are Natural numbers and p is prime
 - set q = p^s 
 - set n = q^m-1 
 - set t = r/2
 - Pick a primitive n'th root of unity, w in F_q^m
 - Pick uniformly at random a permutation of n elements, sigma
 - Set x = (w^sigma(0),w^sigma(1),..,w^sigma(n-1))
 - Let GRS_r(x,x) be the GRS code over F_q^m with dimension r, evaluation points x and column multiplier x
 - Pick a generator matrix G of the alternant code: GRS_r(x, x)^perp intersected with (F_q)^n
   (This is a BCH code with delta = r+1, where the entries of the codewords have been permuted according to sigma)
 - Set t = r/2 (the error correcting capability of GRS_r(x, x)^perp)
 - Return (sk, pk), where sk = x and pk = (G,t) 


Our attack takes as input the pk, (G,t) and outputs a vector y such that G is a generator matrix for 
GRS_r(y, y)^perp intersected with (F_q)^n
I.e. y can act the same as the secret key, x.
More precisely: The decoding algorithm for the code GRS_r(y, y)^perp can be used to decrypt messages. 


To run the attack, ask Magma to load the file "Executable.magma". 
If you want to change parameters, change the code in "Executable.magma" (example parameters are given). 
"Executable.magma" runs "Attack.magma", which gathers all the steps of the attack. 
The remaining magma files are called upon by "Attack" as they are needed. 
The file "results.csv" gathers the results from the attack (timings, number of solutions found etc.)

In the folder "FindingL" we have collected the code to find L and a collection of L's for different parameters.
