url="http://mizar.voksenlia.net/Variable/Redukvis/U-gem"
files="64-65.MAG 65-66.MAG 66-67.MAG 67-68.MAG 68-69.MAG 69-70.MAG 70-71.MAG 71-72.MAG 72-73.MAG 73-74.MAG 74-75.MAG 75-76.MAG 76-77.MAG 77-78.MAG 78-79.MAG 79-80.MAG 80-81.MAG 81-82.MAG 82-83.MAG 83-84.MAG 84-85.MAG 85-86.MAG 86-87.MAG 87-88.MAG 88-89.MAG 89-90.MAG 90-91.MAG 91-92.MAG 92-93.MAG 93-94.MAG 94-95.MAG 95-96.MAG 96-97.MAG 97-98.MAG 98-99.MAG"

for file in $files
do
	#wget $url/$file
	cat $file | grep "<" | tr "<" " "  >> data.txt
done
