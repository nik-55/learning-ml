NLP Tasks
- Named Entity Recognition (NER)
- Part of Speech Tagging (POS)
- Text Classification
- Text Summarization
- Text Generation
- Machine Translation
- Question Answering
- Sentiment Analysis
- speech to text
- text to speech
- text to image
- image to text

Sequence to Sequence data - 

Encoder decoder Architecture [2014]
- Uses LSTM

Attention Mechanism [2015]

Transformer Architecture [2017]
- Two tranformers based Language Models
- BERT - Bidirectional Encoder Representations from Transformers [Google]
- GPT - Generative Pre-Training [OpenAI]

When this model is trained on a large corpus of text, such models are called Large Language Models. 


Transfer Learning [2018] 
- Can be used for NLP tasks for the first time
- Fine tuning
- Language Model - The model learns the language by predicting the next word in a sentence. It is excellent for the pretraining of the model
- Unsupservised pretraining
- LLMs can be fine tuned for a specific task by adding a task specific layer on top of the LLMs and then training the model on the task specific dataset. This can produce state of the art results on the task specific dataset


GPT is fined tuned by the OpenAI team for the chatGPt task. The model is fine tuned for the chatbot task. They also add the context retentive layer to the model.


-----

CNN - Convolutional Neural Network

RNN - Recurrent Neural Network
- Used for sequential data

```python
from keras.layers import SimpleRNN
from keras.models import Sequential

model = Sequential()
model.add(SimpleRNN(32, input_shape=(10, 100)))

```

----

Transformer
- Before transformer, the RNNs were used for the NLP tasks. RNNs are sequential models and they are slow to train. Also, they are not parallelizable. They are also not able to capture the long term dependencies in the text.
- Then LSTMs were used. LSTMs are also sequential models and they are slow to train. Also, they are not parallelizable. They are able to capture a little bit of long term dependencies in the text.  

- Transformers are parallelizable and they are able to capture the long term dependencies in the text. They are also faster to train.

---

Neural Networks - Tabular Data
Convolutional Neural Networks - Images
Recurrent Neural Networks - Sequential Data - LSTM, GRU
Sequence to Sequence data [seq2seq] - Input and Output are both sequences - Encoder Decoder Architecture - Translation


