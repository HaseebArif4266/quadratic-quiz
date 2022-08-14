import cmath

a = 2
b = 5
c = 3

#calculate the discriminate

d = (b**2)-(4*a*c)

# find two solution 

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("the solution are {0} and {1}".format(sol1,sol2))

#in JavaScript

function quadratic(a, b, c){
    let x = (-b - Math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);
    let y = (-b + Math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);
    return[x,y];
}
console.log ('the root of the equation are' + quadratic(2, 5, -6));
