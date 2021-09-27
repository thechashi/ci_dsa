import timer as t

def test_timer():
	start = t.timer()
	end = start.toc()
	print(end)

if __name__ == "__main__":
	test_timer()
