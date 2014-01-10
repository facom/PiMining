all:
	g++ pi.cpp -o pi.out

clean:
	rm -rf *~
	rm -rf *.pyc
	rm -rf *.o *.out *.log

#ONLY FOR CONTRIBUTORS
commit:
	git commit -am "Commit"
	git push master
