# Quantum Data Encoding and PCA

This repository provides a web application for applying data encoding techniques and Quantum Principal Component Analysis (QPCA) to datasets. The application is built using Flask and provides options for amplitude encoding, angle encoding, and quantum PCA.

## Prerequisites

Make sure you have Python 3.11.9 and the required packages installed. You can install the dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### `requirements.txt` includes:
- Flask 3.0.3
- numpy 1.26.4
- pandas 2.2.2
- qiskit 1.1.2
- qiskit-machine-learning 0.7.2

## File Descriptions

### `app.py`
The main Flask application file. It defines routes for:
- The home page (`/`)
- PCA operations (`/pca`)
- Handling file uploads and processing (`/get_columns`, `/process`)
- Performing Quantum PCA (`/qpca`)

### `amplitude_encoding.py`
Defines functions for amplitude encoding of data. This technique normalizes numeric columns of a DataFrame.

### `angle_encoding.py`
Contains functions to apply angle encoding using Rx, Ry, and Rz rotation matrices. This is used for encoding numeric columns into quantum gates.

### `qpca.py`
Provides functions to perform Quantum PCA using Qiskit. It includes:
- `run_qiskit_qpca`: Runs quantum PCA on the provided data
- `perform_quantum_pca`: Integrates with Qiskit to perform PCA and return the reduced dataset

## Usage

1. **Run the Flask Application:**

   To start the Flask app, use the following command:

   ```bash
   python app.py
   ```

2. **Home Page (`/`):** Upload your data files and select encoding or PCA options.

3. **PCA Page (`/pca`):** Access the PCA functionalities.

4. **Data Processing:**
   - Upload a CSV file.
   - Select columns to drop if needed.
   - Choose encoding operations (Amplitude Encoding, Angle Encoding).
   - Download the processed files.

5. **Quantum PCA:**
   - Upload a CSV file.
   - Exclude columns as needed.
   - Specify the number of principal components.
   - Download the Quantum PCA results.

## HTML Templates

The application uses HTML templates located in the `templates` folder:
- `index.html` - Home page
- `pca.html` - PCA page

---

Let me know if there's anything else you'd like to adjust!
