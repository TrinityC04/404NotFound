import {
    BrowserRouter,
    Navigate,
    Route,
    Routes,
} from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import { useAuth } from "./services/AuthProvider";

function Dashboard() {
    const {
        username,
        roles,
        logout,
    } = useAuth();

    return (
        <main>
            <h1>AML Risk Intelligence Platform</h1>
            <h2>Authenticated</h2>
            <p>Welcome, {username}</p>
            <p>Roles: {roles.join(", ")}</p>
            <button onClick={logout}>Logout</button>
        </main>
    );
}

function ProtectedRoute() {
    const {
        initialized,
        authenticated,
    } = useAuth();

    if (!initialized) {
        return <p>Loading authentication...</p>;
    }

    if (!authenticated) {
        return <Navigate to="/login" replace />;
    }

    return <Dashboard />;
}

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route
                    path="/dashboard"
                    element={<ProtectedRoute />}
                />
                <Route
                    path="*"
                    element={<Navigate to="/login" replace />}
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
