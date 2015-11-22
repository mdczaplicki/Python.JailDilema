function decision = MC_decision(penalty)
str_pen = int2str(penalty);
[~, output] = system(['python script.py ' str_pen]);

decision = output;

