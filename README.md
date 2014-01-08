embedded-esoteric
=================

Set of esoteric languages interpreters embedded in python3 code.

If you'd like to contribute, feel free! Just ask me to give you access to repo.
Best way to do this is by mail: filip(dot)malczak(at)gmail(dot)com.
Also, any comment on coding style, ideas, feedback, etc is welcome.

Status:
- Brainfuck works and is quite clean; it needs some annotations, to be cuter,
    and some debugging utils are coming, but for now I focus on Befunge93
- Brainfork will need some changes in AbstractBrainf__kInterpreter; also, because
    of GIL, should we use multiprcessing or threading fot 'Y' instruction?
- Befunge93 is WIP, older versions and other funges will come - maybe; at the
    moment only simplest "hello world" works, and there are some issues with
    input

