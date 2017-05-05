from database import db 
from database import check
from commands import memory, cpu, disk, sshd
import time

db.create_all()
i=1
while True:

	if (i > 100): 
		delete = check.query.first()
		db.session.delete(delete)
		db.session.commit()
		

	ch= check (memory(),cpu(), disk(), sshd())
	db.session.add(ch)
	db.session.commit()
	i=i+1

	time.sleep(60)
