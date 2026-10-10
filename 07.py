from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Apply Min-Max Scaling or Standardization (choose one)
scaler = MinMaxScaler()  # For normalization
# scaler = StandardScaler()  # For standardization

# Scale numerical columns
dataset_scaled = dataset.copy()
dataset_scaled[numerical_columns] = scaler.fit_transform(dataset_scaled[numerical_columns])

print("\nDataset with Scaled Numerical Features:")
print(dataset_scaled.head())
