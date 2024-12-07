function power_test

    for n = 4:4:20

        A = hilbert(n);
        
        tic
        e = eig(A);
        toc
        
        Nmax = 100;
        
        tic
        [lam, ~]= powerIt(A,Nmax);
        toc
        
        err = abs(lam-max(e));
        
        N = 1:Nmax;
        
        figure
        semilogy(N,err,'o-')
        title(sprintf('%i x %i',n,n))
        xlabel('Iterations')
        ylabel('Abs Error')

    end

return


function [lam, v]= powerIt(A,Nmax)
    
    n = size(A,1);
    
    q = rand(n,1);
    q = q/norm(q);
    lam = zeros(Nmax,1);
    
    for j = 1:Nmax
        
       z = A*q;
       q = z/norm(z);
       lam(j) = q'*A*q;
    
    end
    
    v = q;

return

function [H] = hilbert(n)
    
    H = ones(n);
    for i = 1:n
        for j = 1:n
            H(i,j) = 1/(i+j-1);
        end

    end

return