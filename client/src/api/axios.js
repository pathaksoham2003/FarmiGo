import axios from 'axios';

// Create an instance of axios
const axiosInstance = axios.create({
  baseURL: 'https://your-api-base-url.com', // Replace with your API URL
});

// Request interceptor to attach the token
axiosInstance.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');  // Retrieve the token from localStorage
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;  // Attach the token to the Authorization header
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle token expiration or errors
axiosInstance.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response.status === 401) {
      // Handle token expiration, logout, or token refresh logic
      localStorage.removeItem('token');
      window.location.href = '/login';  // Redirect to login page if necessary
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
