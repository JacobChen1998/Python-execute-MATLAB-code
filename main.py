import matlab
import matlab.engine

eng = matlab.engine.start_matlab()
eng.test(nargout=0)