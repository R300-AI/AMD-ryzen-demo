import quark, argparse
from quark.onnx import QuantType, ModelQuantizer
from quark.onnx.quantization.config.config import Config, QuantizationConfig

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--onnx_model", type=str, help="Path to .onnx")
args = parser.parse_args()

quant_config = QuantizationConfig(
    quant_format=quark.onnx.QuantFormat.QDQ,
    calibrate_method=quark.onnx.PowerOfTwoMethod.MinMSE,
    input_nodes=[],
    output_nodes=[],
    op_types_to_quantize=[],
    extra_op_types_to_quantize=[],
    per_channel=False,
    reduce_range=False,
    activation_type=quark.onnx.QuantType.QInt8,
    weight_type=quark.onnx.QuantType.QInt8,
    nodes_to_quantize=[],
    nodes_to_exclude=[],
    subgraphs_to_exclude=[],
    optimize_model=True,
    use_dynamic_quant=False,
    use_external_data_format=False,
    execution_providers=['VitisAIExecutionProvider'],
    enable_npu_cnn=True,
    enable_npu_transformer=False,
    convert_fp16_to_fp32=False,
    convert_nchw_to_nhwc=False,
    include_cle=False,
    include_sq=False,
    include_rotation=False,
    extra_options={'UseRandomData': True}
)

config = Config(global_quant_config=quant_config)
quantizer = ModelQuantizer(config)
quantized_model_path = args.onnx_model.replace('.onnx', '_quant.onnx')
quantizer.quantize_model(model_input = args.onnx_model,
                         model_output = quantized_model_path,
                         calibration_data_path = None)

print('Quantized model saved to:', quantized_model_path)