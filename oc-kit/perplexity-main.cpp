// Reuse the already-built implementation without rebuilding the llama.cpp tree.
int llama_perplexity(int argc, char ** argv);
int main(int argc, char ** argv) { return llama_perplexity(argc, argv); }
