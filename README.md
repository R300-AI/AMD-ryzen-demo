# The Best Implementation for Ryzen AI

AMD Ryzen是一個專門為個人助理打造的AI Processor ，其最大的賣點在於其透過Infinity Fabric晶片互連技術，將CPU, GPU及NPU整合於單一張晶片中(APU)，使它們能透過[共享同一個內存池(Unified Memory)](https://www.amd.com/en/developer/resources/technical-articles/2025/amd-ryzen-ai-max-395--a-leap-forward-in-generative-ai-performanc.html)來將資料傳輸效率最佳化，適合用於部署Hybrid Execution的應用。

其複雜的系統成分也意味著它的軟體支援性將成為應用開發上的一大挑戰。因此，這個Repository的目的便是在於持續追蹤AMD Ryzen官方軟體支援的資訊，為一般**AI研究人員**或**早期概念驗證的開發者**提供最新且完整的軟體安裝流程。這些軟體主要是使用[Windows11作業系統](https://www.microsoft.com/zh-tw/software-download/windows11)(*Linux仍在實驗階段*)，且必須透過[Conda](https://www.anaconda.com/docs/getting-started/miniconda/main)來布置這些軟體的虛擬環境。除此之外，我們也特別針對一些常見的Python Execution提供範例模板，以此加速Ryzen AI生態的應用創新。

您可以透過點擊以下連結來播放並學習Ryzen AI基礎知識的介紹影片(大約半小時)：

<div align="center">
  
:point_right: [AMD Ryzen™ AI Tutorials](https://youtube.com/playlist?list=PLYw1WVX5aNHABNAfottruTY8oX2eFlzmz&si=RLDuVowcy-6znu3e)

</div>

## 安裝相依套件

1. 下載並安裝舊版[Visual Studio 2022](https://download.microsoft.com/download/2/E/6/2E61CFA4-993B-4DD4-91DA-3737CD5CD6E3/vcredist_x64.exe)及**使用C++的桌面開發**元件
  
2. 下載並安裝[cmake x64 Installer](https://cmake.org/download/)

2. 安裝Ryzen AI `Radeon iGPU` 所需的相依套件。
```bash
pip install -r requirements.txt
```

### 將Ryzen AI配置為工作站

  AMD Ryzen APU雖然已經搭載了完整的internal GPU(=iGPU)及NPU，但是這些處理器僅支援與"推論"有關的程序，針對"訓練"方面的工作仍只能依靠內建的CPU。或者，您也可以透過主機板的外部擴充卡槽(如：[Radeon Graphics Cards](https://www.amd.com/en/products/graphics/desktops/radeon.html))來增強本機在訓練模型、微調神經網路參數的能力。

## Installation

<div align="center">
<table><thead>
  <tr>
    <th>Task</th>
    <th colspan="2">Inference/Training</th>
    <th colspan="5">Inference only</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Tools</td>
    <td colspan="4">Jupyter/ VS Code...etc</td>
    <td colspan="3">GAIA</a></td>
  </tr>
  <tr>
    <td>Usage</td>
    <td>All</td>
    <td colspan="3">General CNNs/ Transformers</td>
    <td colspan="3">LLMs</td>
  </tr>
  <tr>
    <td>Runtime</td>
    <td colspan="6">Python==3.10&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td rowspan="2">C++</td>
  </tr>
  <tr>
    <td>Framework</td>
    <td>Torch/TF/JAX</td>
    <td colspan="3">
      <a href="https://github.com/onnx/digestai"><b>ONNX with Digest AI</b></a> 
    </td>
    <td colspan="2">Lemonade CLI</td>
  </tr>
  <tr>
    <td>Software</td>
    <td rowspan="2">
      <a href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html"><b>ROCm and Driver<br>(using WSL)</b></a> 
    </td>
    <td colspan="6">
      <a href="https://ryzenai.docs.amd.com/en/latest/inst.html"><b>Ryzen AI Software (包括下列Provider及Quark)</b></a> 
    </td>
  </tr>
  <tr>
    <td>Execution Provider</td>
    <td>--</td>
    <td>DirectML</td>
    <td>VitisAI</td>
    <td colspan="3">OGA</td>
  </tr>
  <tr>
    <td>Processor Type</td>
    <td>external GPUs</td>
    <td>CPU</td>
    <td>iGPU</td>
    <td>NPU</td>
    <td colspan="3">Hybrid</td>
  </tr>
</tbody>
</table>
</div>

上方提供的表格為AMD官方提供的資源清單及應用方式，請依照自己的Processor及Usage識別相對應所需使用的軟體，並依照由下而上的順序逐步進行安裝。
> [!TIP]
> External GPUs目前僅支援Linux作業系統。因此，您需要額外透過[WSL](https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/)安裝Ubuntu24.04或其他可支援的系統版本，才能安裝與調用Driver與ROCm這些資源。

## How to Use This?

### **External GPUs (in WSL)**

ROCm為AMD Radeon系列的API與軟體，開發者可以利用這些工具調度GPUs中的運算單元，用於加速可平行化處理的運算工作。這個軟體能夠支援一般的深度學習開發框架與C++/Python開發工具，讓開發者可以輕易地加速設計、訓練及調適AI模型的過程。

為此，您可以依照下列這些文件來安裝它們，並在個別的開源社群瞭解這些框架的使用方法：

* 安裝深度學習框架 | [PyTorch](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html), [Tensorflow](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html), [JAX](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html)
* 安裝程式開發工具     | [Jupyter (for Python)](https://jupyter.org/install), [VS Code](https://code.visualstudio.com/download)

### **CPU, GPU and NPU**

1. Ryzen AI處理器是透過ONNX解釋器來辨認模型的神經網路架構及運算參數，所以得先將PyTorch、Tensorflow或JAX設計好的模型輸出成ONNX格式(建議輸出的opset版本為13)，才能將其委託到CPU, GPU及NPU上做推論。
   > 請先下載這個範例程式庫，在`./models`中已經有預先輸出一些`.onnx`模型，您可以透過[Netron](https://github.com/lutzroeder/netron)或[Digest AI](https://github.com/onnx/digestai)來預覽檔案的成分。
   > ```bash
   > $ git clone https://github.com/R300-AI/AMD-ryzen-demo.git && cd AMD-ryzen-demo
   > $ conda activate ryzen-ai-1.4.0      # 這個環境會與Ryzen AI software一起被安裝到您的主機.
   > ```

2. 如果要將模型部署到NPU，您需要先透過Quark工具將ONNX檔中可量化的運算子編譯為NPU的操作指令。(請注意，由於NPU僅支援少部分可平行化的運算子，所以其它的基礎操作仍會保留在CPU上執行)
   > 您可以透過編輯`onnx_quantizer.py`中的`quant_config`來變更量化方法，詳細的參數配置請參閱[官方文件]。(https://quark.docs.amd.com/latest/onnx/appendix_full_quant_config_features.html)。
   > ```bash
   > $ python onnx_quantizer.py --onnx_model ./models/yolov8n.onnx    # 編譯後的模型預設會輸出於<onnx_model>_quant.onnx
   > ```

4. 接下來展示如何使用原生的ONNX Runtime將模型委託至指定的處理器做加速推論。
   > `--provider`的選項分別為`CPUExecutionProvider`、`DmlExecutionProvider`及`VitisAIExecutionProvider`
   > ```bash
   > $ python onnx_benchmark.py --onnx_model ./models/yolov8n.onnx --provider CPUExecutionProvider
   > ```

## LLM Toolkits
AMD LLM Toolkit 提供完整的本地大型語言模型 (LLM) 推論解決方案，涵蓋從高階應用到底層 API 的不同需求。主要包含兩個工具：

- **GAIA**：Ryzen AI 官方應用程式，適合一般使用者，提供圖形介面 (UI) 與命令列 (CLI) 操作，能體驗各類 AI 代理任務（如聊天、影片分析、文字生成等）。
- **Lemonade**：專為開發者設計的 LLM 推論 API，支援 Python 及 CLI，方便整合至自訂應用或自動化流程。

兩者皆可充分發揮 Ryzen AI 平台的異質運算優勢，支援多種硬體加速模式，協助用戶根據需求選擇最佳化的推論效能與能耗表現。

<div align="center">
<table border="1">
    <thead>
        <tr>
            <th colspan="2">項目</th>
            <th>GAIA</th>
            <th>Lemonade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2"><strong>用途</strong></td>
            <td>高階的 LLM 代理任務</td>
            <td>LLM後端推論的API</td>
        </tr>
        <tr>
            <td colspan="2"><strong>運作方式</strong></td>
            <td>透過 <strong>UI</strong> 或 <strong>CLI</strong> 與 LLM 互動</td>
            <td>支援 <strong>Python API</strong> 及 <strong>CLI</strong></td>
        </tr>
        <tr>
            <td rowspan="3"><strong>硬<br>體<br>加<br>速</strong></td>
            <th>混合模式 (Hybrid Mode)</th>
            <td colspan="2">性能最佳, 使用OGA來混合調用<strong>NPU + iGPU</strong> 加速 LLM 運算</td>
        </tr>
        <tr>
            <th>NPU 模式 (NPU Mode)</th>
            <td colspan="2">能耗最佳, 使用OGA來調用<strong>NPU</strong> 加速 LLM 運算</td>
        </tr>
        <tr>
            <th>通用模式 (Generic Mode)</th>
            <td colspan="2">在所有CPU上皆能使用，OGA可以替換為 Ollama</td>
        </tr>
    </tbody>
</table>
</div>

### 安裝資源

- [GAIA 安裝說明](https://github.com/amd/gaia)
- [Lemonade 安裝說明](https://github.com/lemonade-sdk/lemonade/blob/main/docs/README.md)

> **注意**：安裝 GAIA 時會自動包含 Lemonade；Lemonade 也可獨立安裝使用。
