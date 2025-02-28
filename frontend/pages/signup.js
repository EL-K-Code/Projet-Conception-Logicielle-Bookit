"use client";
import Form from "../components/Form";

export default function SignUp() {
    return <Form route="/api/auth/signup/" method="signup" />;
}
