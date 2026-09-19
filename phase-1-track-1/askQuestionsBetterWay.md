"Is there a DSA pattern I've already mastered that describes the shape of this problem?

If yes, name it explicitly in a comment or your own notes (like your DSA doc already does with "Mental Model: Explorer and Boundary"). That act of naming is what cements the cross-connection — it's the same reflection principle as Polya's method, just pointed outward at your projects instead of inward at the DSA problem itself.

This is genuinely how you get to "500 cross-domain connections" faster than just doing both tracks in parallel and hoping they merge on their own

# Never ask like this

- How can I build an n-dimensional vector in Python?
- This often leads to someone else's implementation.

# 1. What → Understand the concept

Examples:

✅ What is an n-dimensional vector?
✅ What responsibilities should a Vector class have?
✅ What makes two vectors equal?
✅ What edge cases exist for vector addition?

# 2. Why → Understand the reasoning

Examples:

✅ Why do most libraries store vector components in a list?
✅ Why should vector addition return a new object?
✅ Why is the zero vector valid?
✅ Why does matrix multiplication require compatible dimensions?

# 3. Should → Make design decisions

Examples:

✅ Should Vector be mutable?
✅ Should Matrix contain Vector objects?
✅ Should I expose components publicly?
✅ Should **mul** support vector × vector?

These are some of the most valuable questions for becoming a good software designer.

# 4. When → Learn best practices

Examples:

✅ When should I implement **iter**?
✅ When should I raise TypeError?
✅ When should I use a property instead of a public attribute?

# 5. How → Learn implementation

Use this last, after you understand the concept and design.

Examples:

✅ How does **iter** work?
✅ How does zip() pair elements?
✅ How does **matmul** work in Python?
