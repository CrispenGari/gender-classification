# Gender Classification

This is a simple `REST` api that is served to classify gender on an image given based on faces.

 <p align="center" with="100%"><img src="/faces.jpg" width="100%" alt=""/>
</p>

### Starting the server

To run this server and make prediction on your own images follow the following steps

1. create a virtual environment and activate it
2. run the following command to install packages

```shell
pip install -r requirements.txt
```

3. navigate to the `app.py` file and run

```shell
python app.py
```

### Model Metrics

The following table shows all the metrics summary we get after training the model for few `6` epochs.

<table border="1">
    <thead>
      <tr>
        <th>model name</th>
        <th>model description</th>
        <th>test accuracy</th>
        <th>validation accuracy</th>
        <th>train accuracy</th>
         <th>test loss</th>
        <th>validation loss</th>
        <th>train loss</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>gender-classification</td>
        <td>classification of intents by a chatbot.</td>
        <td>95.04%</td>
        <td>91.59%</td>
        <td>91.59%</td>
        <td>0.1273</td>
        <td>0.2593</td>
        <td>0.2593</td>
      </tr>
       </tbody>
  </table>

### Classification report

This classification report is based on the first batch of the validation dataset i used which consist of 32 images.

precision recall f1-score support

<table border="1">
    <thead>
      <tr>
        <th>#</th>
        <th>precision</th>
        <th>recall</th>
        <th>f1-score</th>
        <th>support</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>accuracy</td>
        <td></td>
        <td></td>
        <td>100%</td>
        <td>512</td>
      </tr>
      <tr>
        <td>macro avg</td>
        <td>100%</td>
        <td>100%</td>
        <td>100%</td>
        <td>512</td>
      </tr>
      <tr>
        <td>weighted avg</td>
        <td>100%</td>
        <td>100%</td>
        <td>100%</td>
        <td>512</td>
      </tr>
    </tbody>
  </table>

### Confusion matrix

The following image represents a confusion matrix for the first batch in the validation set which contains `32` images:

<p align="center" with="100%"><img src="/faces.jpg" width="100%" alt=""/>
</p>

### Gender classification

If you hit the server at `http://localhost:3001/api/gender` you will be able to get the following expected response that is if the request method is `POST` and you provide the file expected by the server.

### Expected Response

The expected response at `http://localhost:3001/api/gender` with a file `image` of the right format will yield the following `json` response to the client.

```json
{
  "predictions": {
    "class": "male",
    "label": 1,
    "meta": {
      "description": "classifying gender based on the face of a human being, (vgg16).",
      "language": "python",
      "library": "tensforflow: v2.*",
      "main": "computer vision (cv)",
      "programmer": "@crispengari"
    },
    "predictions": [
      {
        "class": "female",
        "label": 0,
        "probability": 0.019999999552965164
      },
      {
        "class": "male",
        "label": 1,
        "probability": 0.9800000190734863
      }
    ],
    "probability": 0.9800000190734863
  },
  "success": true
}
```

### Using `curl`

Make sure that you have the image named `female.jpg` in the current folder that you are running your `cmd` otherwise you have to provide an absolute or relative path to the image.

> To make a `curl` `POST` request at `http://localhost:3001/api/gender` with the file `female.jpg` we run the following command.

```shell
curl -X POST -F image=@female.jpg http://127.0.0.1:3001/api/gender
```

### Using Postman client

To make this request with postman we do it as follows:

1. Change the request method to `POST`
2. Click on `form-data`
3. Select type to be `file` on the `KEY` attribute
4. For the `KEY` type `image` and select the image you want to predict under `value`
5. Click send

If everything went well you will get the following response depending on the face you have selected:

```json
{
  "predictions": {
    "class": "male",
    "label": 1,
    "meta": {
      "description": "classifying gender based on the face of a human being, (vgg16).",
      "language": "python",
      "library": "tensforflow: v2.*",
      "main": "computer vision (cv)",
      "programmer": "@crispengari"
    },
    "predictions": [
      {
        "class": "female",
        "label": 0,
        "probability": 0.019999999552965164
      },
      {
        "class": "male",
        "label": 1,
        "probability": 0.9800000190734863
      }
    ],
    "probability": 0.9800000190734863
  },
  "success": true
}
```

### Using JavaScript `fetch` api.

1. First you need to get the input from `html`
2. Create a `formData` object
3. make a POST requests

```js
const input = document.getElementById("input").files[0];
let formData = new FormData();
formData.append("image", input);
fetch("http://localhost:3001/predict", {
  method: "POST",
  body: formData,
})
  .then((res) => res.json())
  .then((data) => console.log(data));
```

If everything went well you will be able to get expected response.

```json
{
  "predictions": {
    "class": "male",
    "label": 1,
    "meta": {
      "description": "classifying gender based on the face of a human being, (vgg16).",
      "language": "python",
      "library": "tensforflow: v2.*",
      "main": "computer vision (cv)",
      "programmer": "@crispengari"
    },
    "predictions": [
      {
        "class": "female",
        "label": 0,
        "probability": 0.019999999552965164
      },
      {
        "class": "male",
        "label": 1,
        "probability": 0.9800000190734863
      }
    ],
    "probability": 0.9800000190734863
  },
  "success": true
}
```

### Notebooks

The `ipynb` notebook that i used for training the model and saving an `.h5` file was can be found:

1. [Model Training And Saving](https://github.com/CrispenGari/cv-tensorflow/blob/main/01_Classification/05_Gender_VGG16/01_Gender_Classification_VGG16.ipynb)
