import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "./api";

function Login() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const login = async () => {
    try {
      const formData = new URLSearchParams();
      formData.append("username", form.username.toLowerCase());
      formData.append("password", form.password);

      const response = await api.post("/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      localStorage.setItem("token", response.data.access_token);
      localStorage.setItem("username", form.username.toLowerCase());

      const tokenPayload = JSON.parse(
        atob(response.data.access_token.split(".")[1])
      );

      localStorage.setItem("role", tokenPayload.role);

      navigate("/tickets");
    } catch (error) {
      alert(error.response?.data?.detail || "Login failed");
    }
  };

  return (
    <div className="container mt-4">
      <div className="card p-4 mx-auto" style={{ maxWidth: "500px" }}>
        <h2>Customer Support Login</h2>

        <form
          onSubmit={(e) => {
            e.preventDefault();
            login();
          }}
        >
          <label className="form-label">Username</label>

          <input
            className="form-control mb-3"
            value={form.username}
            onChange={(e) =>
              setForm({
                ...form,
                username: e.target.value,
              })
            }
          />

          <label className="form-label">Password</label>

          <input
            type="password"
            className="form-control mb-3"
            value={form.password}
            onChange={(e) =>
              setForm({
                ...form,
                password: e.target.value,
              })
            }
          />

          <button type="submit" className="btn btn-primary">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;