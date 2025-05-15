import time, argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--onnx_model", type=str, help="Path to .onnx")
parser.add_argument("-d", "--provider", type=str, 
                                        default='CPUExecutionProvider', 
                                        choices = ['CPUExecutionProvider', 'DmlExecutionProvider', 'VitisAIExecutionProvider'], 
                                        help=""
)

args = parser.parse_args()
if args.provider == 'CPUExecutionProvider':
    from utils.provider import CPUExecutionProvider
    session = CPUExecutionProvider(args.onnx_model)
if args.provider == 'DmlExecutionProvider':
    from utils.provider import DmlExecutionProvider
    session = DmlExecutionProvider(args.onnx_model)
if args.provider == 'VitisAIExecutionProvider':
    from utils.provider import VitisAIExecutionProvider
    session = VitisAIExecutionProvider(args.onnx_model)

input_shape = session.get_inputs()[0].shape
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

inputs = np.random.rand(*input_shape).astype(np.float32)
ts = time.time()
for _ in range(1000):
    outputs = session.run([output_name], {input_name: inputs})
print('----------------------------------------')
print('Output shape: ', outputs[0].shape)
print('Inference time: ', str((time.time() - ts)), " ms")
print('----------------------------------------')