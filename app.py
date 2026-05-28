import streamlit as st
st. title ('나는 짱이다')
st. write ('바이브코딩 재미있다!')
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

app.post("/coach", async (req, res) => {
  try {
    const { message } = req.body;

    const completion = await openai.chat.completions.create({
      model: "gpt-4.1-mini",
      messages: [
        {
          role: "system",
          content: `
너는 전문 연애 코치다.
사용자의 연애 고민을 분석하고:
- 감정 분석
- 상대 심리 추론
- 카톡 답장 추천
- 데이트 전략
- 관계 개선법
을 친절하게 설명해라.
`,
        },
        {
          role: "user",
          content: message,
        },
      ],
    });

    res.json({
      reply: completion.choices[0].message.content,
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({
      error: "AI 응답 실패",
    });
  }
});

app.listen(3000, () => {
  console.log("Server running on 3000");
});
