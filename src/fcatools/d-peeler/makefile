NAME = d-peeler
CXX = g++ -O3 -flto -Wall -Wextra -Weffc++ -std=c++11 -pedantic -Wno-unused-parameter -Wno-ignored-qualifiers
EXTRA_CXXFLAGS = -lboost_program_options -flto
SRC = src
DEPS = $(wildcard $(SRC:=/*.h)) Parameters.h makefile
CODE = $(wildcard $(SRC:=/*.cpp))
OBJ = $(CODE:.cpp=.o)
ALL = $(DEPS) $(CODE) COPYING example INSTALL README

.PHONY: install clean dist-gzip dist-bzip2 dist-xz dist
.SILENT: $(NAME) install clean dist-gzip dist-bzip2 dist-xz dist

%.o: %.cpp $(DEPS)
	$(CXX) -c -o $@ $<

$(NAME): $(OBJ)
	$(CXX) -o $@ $^ $(EXTRA_CXXFLAGS)
	echo "$(NAME) built!"

install: $(NAME)
	mv $(NAME) /usr/bin
	echo "$(NAME) installed!"

clean:
	rm -f $(patsubst %,%/*.o,$(SRC)) $(patsubst %,%/*~,$(SRC)) *~

dist-gzip:
	tar --format=posix --transform 's,^,$(NAME)/,' -czf $(NAME).tar.gz $(ALL)

dist-bzip2:
	tar --format=posix --transform 's,^,$(NAME)/,' -cjf $(NAME).tar.bz2 $(ALL)

dist-xz:
	tar --format=posix --transform 's,^,$(NAME)/,' -cJf $(NAME).tar.xz $(ALL)

dist: dist-bzip2
