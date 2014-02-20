var total = 0, total2 = 0, total3=0, grandtotal=0;

for (var x = 0; x < 1000; x+=1){
	if (x%3==0){
		total+=x;
	} else if (x%5==0){
		total+=x;
	}
}

console.log(total);